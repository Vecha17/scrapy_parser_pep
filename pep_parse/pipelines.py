import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.peps = {}
        self.result = [('Статус', 'Количество'), ]
        self.total = 0

    def process_item(self, item, spider):
        self.total += 1
        if item['status'] in self.peps:
            self.peps[item['status']] += 1
        else:
            self.peps[item['status']] = 1
        return item

    def close_spider(self, spider):
        for key, value in self.peps.items():
            self.result.append(
                (key, value)
            )
        self.result.append(('Total', self.total))
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.result)
