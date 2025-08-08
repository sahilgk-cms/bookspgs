import csv
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookspgs.settings')
django.setup()

from django.db import connection

# File paths
BOOK_CSV = 'booktable.csv'
USER_CSV = 'usertable.csv'
RATING_CSV = 'userratingtable.csv'

def load_csv_to_table(csv_file, table_name, columns):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with connection.cursor() as cursor:
        for row in rows:
            values = [row[col] for col in columns]
            placeholders = ', '.join(['%s'] * len(values))
            query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
            try:
                cursor.execute(query, values)
            except Exception as e:
                print(f'Error inserting into {table_name}: {e}')
                continue

    print(f"✅ Loaded {len(rows)} records into {table_name}")

def main():
    print("📦 Starting data import...")

    load_csv_to_table(
        BOOK_CSV,
        'booktable',
        ['book_id', 'title', 'authors', 'average_rating', 'isbn', 'isbn13',
         'language_code', 'num_pages', 'ratings_count', 'text_reviews_count',
         'publication_date', 'publisher']
    )

    load_csv_to_table(
        USER_CSV,
        'usertable',
        ['user_id', 'username']
    )

    load_csv_to_table(
        RATING_CSV,
        'userratingtable',
        ['user_id', 'book_id', 'rating']
    )

    print("🎉 All data loaded!")

if __name__ == '__main__':
    main()