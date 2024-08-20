AUTHOR = "Golod D., Polyak M."
SITENAME = "Polyak M.S."
SITEURL = ""

PATH = "content"
STATIC_PATHS = ("images", "books", "extra")
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
THEME = "themes/lovers"
# BOOTSTRAP_THEME = "lovers"

TIMEZONE = "Europe/Moscow"

DEFAULT_LANG = "RU"

ARTICLE_URL = "poliak-mark-solomonovich.html"

SOCIAL = (("mail", "mailto:mspolyak@ya.ru"),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Naviagtion
NAV_MENU_CONTENT = (("Домой", "index.html"), ("Публикации", "publications.html"))

# Current books
BOOKS = (
    (
        "Поляк М.С. Сочетанная антибиотикотерапия",
        "books/combined_antibiotic_therapy.pdf",
        "combined_antibiotic_therapy_book_small_tn.jpg",
    ),
    (
        "Поляк М.С. Антибиотики в лечении анаэробных заболеваний",
        "books/antibiotics_in_treatment_of_anaerobes.pdf",
        "antibiotics_in_treatment_of_anaerobes_book_small_tn.jpg",
    ),
    (
        "Информация о книге",
        "books/present_day_problems_of_antibiotic_therapy_in_ophthalmology.pdf",
        "antibiotic_therapy_in_ophthalmology_book_small_tn.jpg",
    ),
    (
        "Информация о книге",
        "antibiotics_in_ophthalmology.html",
        "antibiotics_in_ophthalmology_book_small_tn.jpg",
    ),
    (
        "Информация о книге",
        "antibiotic_therapy_of_problematic_infections.html",
        "antibiotics_overcoming_resistance_book_small_tn.jpg",
    ),
    (
        "Информация о книге",
        "antibiotics_laboratory_book.html",
        "antibiotics_laboratory_book_small_tn.jpg",
    ),
    (
        "Информация о книге",
        "antibiotic_therapy_theory_and_practice_book.html",
        "antibiotics_book_small_tn.jpg",
    ),
    (
        "Питательные среды для медицинской и санитарной микробиологии",
        "culture_media_2008_book.html",
        "culture_media_book_small_tn.jpg",
    ),
)

DEFAULT_PAGINATION = 10

PROFILE_PICTURE = "mspolyak_photo_tn.jpg"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
