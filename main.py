from url_checker import check_url
from domain_checker import check_domain
from email_checker import check_email


def verdict(score):
    if score >= 6:
        return "🚨 Likely Phishing"
    elif score >= 3:
        return "⚠️ Suspicious"
    else:
        return "✅ Safe"


def url_feature():
    url = input("\nEnter URL: ")
    score = check_url(url)

    print("Result:", verdict(score))
    print("Risk Score:", score)


def domain_feature():
    domain = input("\nEnter Domain Name: ")
    score = check_domain(domain)

    print("Result:", verdict(score))
    print("Risk Score:", score)


def email_feature():
    email = input("\nEnter Email Text: ")
    score = check_email(email)

    print("Result:", verdict(score))
    print("Risk Score:", score)


def all_features():
    url = input("\nEnter URL: ")
    domain = input("Enter Domain Name: ")
    email = input("Enter Email Text: ")

    total_score = 0
    total_score += check_url(url)
    total_score += check_domain(domain)
    total_score += check_email(email)

    print("\nFinal Verdict:", verdict(total_score))
    print("Total Risk Score:", total_score)


def main():
    while True:
        print("\n==== PhishGuard Menu ====")
        print("1. Check URL")
        print("2. Check Domain")
        print("3. Check Email Text")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            url_feature()

        elif choice == "2":
            domain_feature()

        elif choice == "3":
            email_feature()

       
        elif choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
