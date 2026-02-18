import sqlite3
import json
import os
import pandas as pd

PWD = os.path.dirname(os.path.abspath(__file__))


def get_attendance_data():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM attendance')
    rows = cursor.fetchall()

    output = []
    for row in rows:
        instance_ = {
            "id": row[0],
            "side": row[1],
            "name": row[2],
            "meal": row[3],
            "count": row[4],
            "timestamp": row[5]
        }
        output.append(instance_)
    conn.close()
    return output


if __name__ == "__main__":
    data = get_attendance_data()
    # Save the data to a JSON file
    with open(os.path.join(PWD, 'attendance_data.json'), 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Save the data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(PWD, 'attendance_data.csv'), index=False, encoding="utf-8")