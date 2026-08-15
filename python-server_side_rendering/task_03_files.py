import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv_products():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            products_list = read_json_products()
        elif source == 'csv':
            products_list = read_csv_products()
    except Exception:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            target_id = int(product_id)
            filtered = [p for p in products_list if p.get('id') == target_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            products_list = filtered
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
