def get_skills():
    return ["C++", "Python", "Java", "Flask", "Qt", "Spring", "Html",
            "CSS", "Bootstrap", "Sql", "pytest", "Data Structures",
            "Algorithms", "Machine Learning", "Git"]


def outside_work_images():
    img_base_url = "../static/assets/images/"
    return [
        {
            "img_url": img_base_url + "gallivanting.jpg",
            "img_alt": "Gallivanting",
            "img_caption": "Gallivanting (Dec 2018)"
        },
        {
            "img_url": img_base_url + "trekking.jpg",
            "img_alt": "Trekking",
            "img_caption": "Trekking (March 2018)"
        },
        {
            "img_url": img_base_url + "group_hangouts.jpg",
            "img_alt": "Group Hangouts",
            "img_caption": "Group Hangouts (March 2018)"
        },
        {
            "img_url": img_base_url + "go_karting.jpg",
            "img_alt": "Go Karting",
            "img_caption": "Go Karting (Dec 2019)"
        },
    ]