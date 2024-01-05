from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.eg/-/en/Honor-fitness-tracker-inches-amoled/product-reviews/B0943WNRVL/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews"

def main(url):
    try:
        # Send a GET request to the specified URL
        page = requests.get(url)

        # Check if the request was successful (status code 200)
        if page.status_code == 200:
            # Parse the HTML content of the page
            src = page.content
            soup = BeautifulSoup(src, "html.parser")

            # Find all review sections on the page
            all_reviews = soup.find_all("div", class_="a-section review aok-relative")

            # Initialize lists to store extracted data
            all_data = []
            for review in all_reviews:
                # Extract individual elements from each review section
                headComment = review.find("span", class_="cr-original-review-content")
                dateOfComment = review.find("span", class_="a-size-base a-color-secondary review-date")
                bodyComment = review.find("span", class_="a-size-base review-text review-text-content")
                stars = review.find("span", class_="a-icon-alt")

                # Handling None values and stripping unnecessary whitespaces
                head_comment_text = headComment.text.strip() if headComment else ""
                date_of_comment_text = dateOfComment.text.strip() if dateOfComment else ""
                body_comment_text = bodyComment.text.strip() if bodyComment else ""
                stars_text = stars.text.strip() if stars else ""

                # Append the extracted data to the list
                all_data.append([head_comment_text, date_of_comment_text, body_comment_text, stars_text])

            # Save the extracted data to a CSV file
            save_to_csv(all_data, "amazon_reviews.csv")
            print("Data saved to amazon_reviews.csv successfully.")

        else:
            print(f"Failed to retrieve the page. Status code: {page.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def save_to_csv(data, filename):
    # Save the extracted data to a CSV file
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # Write header to the CSV file
        writer.writerow(["Head Comment", "Date of Comment", "Body Comment", "Stars"])

        # Write data rows to the CSV file
        writer.writerows(data)

if __name__ == "__main__":
    # Run the main function with the specified URL
    main(url)
