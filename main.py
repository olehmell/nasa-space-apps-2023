import re
import yake
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import openai

api_key = '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'
openai.api_key = api_key


def getReason(keywords):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write as an 3rd person an short summary text why he fits by next data. But call him in 2nd persons. " + keywords,
        temperature=1.25,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


def get_template(person_fits, reason_why_fits_keywords, project_keywords):
    template = f'''
"PersonFits": "{person_fits}",
"ReasonWhyFitsKeywords": "{reason_why_fits_keywords}",
"ProjectKeywords": "{project_keywords}"
'''
    return template


# якщо ви вперше використовуєте nltk, вам може знадобитися завантажити набір стоп-слів за допомогою наступного коду:
# nltk.download('stopwords')
# nltk.download('punkt')

def clean_text(text):
    # Видалити усі спеціальні символи
    text = re.sub(r'\W', ' ', text)

    # Видалити усі одиночні символи
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

    # Замінити більше ніж одного пробілу на один
    text = re.sub(r'\s+', ' ', text, flags=re.I)

    # Перетворити усі букви на маленькі
    text = text.lower()

    # Видалити стоп-слова
    tokens = word_tokenize(text)
    tokens = [i for i in tokens if not i in stopwords.words('english')]
    text = ' '.join(tokens)

    return text


# Read the content of the .txt file
with open("projects.txt", "r") as file:
    projects_json = file.read()

projects = json.loads(projects_json)


# Ваш існуючий код починається тут...

def extract_keywords(text):
    cleaned_text = clean_text(text)
    keywords = kw_extractor.extract_keywords(cleaned_text)
    return [kw[0] for kw in keywords]


# Зчитування даних з файлу і ініціалізація
kw_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='jaccard', windowsSize=1, top=200)

# Допустимо у вас є такий користувач:

with open("user.txt", "r") as file:
    user_Json = file.read()

user = json.loads(user_Json)


user_keywords = set(extract_keywords(user["skills"]) + extract_keywords(user["biography"]))

matches = {}
for project in projects:
    print(f"\nProject: {project['projectName']}\nKeywords:")

    project_keywords = set(extract_keywords(project['description']))
    common_keywords = user_keywords.intersection(project_keywords)
    percentage_match = (len(common_keywords) / len(project_keywords)) * 100 if project_keywords else 0
    matches[project['projectName']] = percentage_match

    # Вивести ключові слова для проекту (ваш існуючий код)
    sorted_keywords = sorted(project_keywords, key=lambda x: x[1], reverse=True)
    for kw in sorted_keywords:
        print(kw)

print("\nPercentage Matches with User Skills and Biography:")
for project, match_percent in matches.items():
    print(f"Project: {project} matches {match_percent:.2f}% with the user's skills and biography.")

user_cleaned_text = clean_text(user["skills"] + " " + user["biography"])
matches = {}
for project in projects:
    project_cleaned_text = clean_text(project['description'])

    # Поділити текст на слова та зробити множину
    user_words = set(user_cleaned_text.split())
    project_words = set(project_cleaned_text.split())
    project_keywords = set(extract_keywords(project['description']))
    # Порівняння словами
    common_words = user_words.intersection(project_words)
    percentage_match = (len(common_words) / len(project_words)) * 100 if project_words else 0

    reasonExplanation = get_template(f"Project: {project} matches {percentage_match:.2f}% with the user's skills and biography.", f"{', '.join(list(common_words))}", f"{', '.join(project_keywords)}")

    matches[project['projectName']] = {
        "match_percentage": percentage_match,
        "reason": getReason(reasonExplanation)
    }

print("\nPercentage Matches with User Skills and Biography:")
for project, match_data in matches.items():
    print(f"Project: {project} matches {match_data['match_percentage']:.2f}% with the user's skills and biography.")
    print(f"Reason: {match_data['reason']}")

