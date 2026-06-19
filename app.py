from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():

    # Read CSV
    df = pd.read_csv("all_books.csv")

    # Clean Price Column
    df["Price"] = df["Price"].astype(str).str.extract(r'(\d+\.\d+)')
    df["Price"] = df["Price"].astype(float)

    # Dashboard Statistics
    total_books = len(df)
    avg_price = round(df["Price"].mean(), 2)
    highest_price = round(df["Price"].max(), 2)
    lowest_price = round(df["Price"].min(), 2)

    # Rating Distribution
    rating_counts = df["Rating"].value_counts().to_dict()

    # Top 10 Expensive Books
    top_books = (
        df.sort_values("Price", ascending=False)
          .head(10)
          .to_dict(orient="records")
    )

    # All Books
    books = df.to_dict(orient="records")

    return render_template(
        "index.html",
        books=books,
        total_books=total_books,
        avg_price=avg_price,
        highest_price=highest_price,
        lowest_price=lowest_price,
        rating_counts=rating_counts,
        top_books=top_books
    )

# Download Dataset Route
@app.route('/download')
def download():
    return send_file(
        "all_books.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)