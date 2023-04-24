import csv

with open('keywords.csv', 'r', encoding="utf-8") as f:
    csv_to_json = csv.DictReader(f)
    json_compiled = [row for row in csv_to_json]

    hasKeyword = [{'movie_id': row['movie_id'], 'id': keyword['id']}
                  for row in json_compiled
                  for keyword in eval(row['keywords'])]
    with open('hasKeyword.cvs', 'w', newline='', encoding="utf-8") as f1:
        writer = csv.writer(f1)

        
        writer.writerow(hasKeyword[0].keys())

        
        for row in hasKeyword:
            writer.writerow(row.values())

    Keyword = [{'id': keyword['id'], 'name': keyword['name']}
               for row in json_compiled
               for keyword in eval(row['keywords'])]

    Keyword_data = []
    distinct_Keyword = set()
    for item in Keyword:
        value = item['id']
        if value not in distinct_Keyword:
            Keyword_data.append(item)
            distinct_Keyword.add(value)

    with open('keyword.csv', 'w', newline='', encoding="utf-8") as f2:
        writer = csv.writer(f2)

        writer.writerow(Keyword_data[0].keys())

        for row in Keyword_data:
            writer.writerow(row.values())
        f2.close()
    f1.close()
f.close()
