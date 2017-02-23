sex = {
    'F': 'Female',
    'M': 'Male',
    'T': 'Transgender'
}
sex_choices = [tuple([v, k]) for k, v in sex.items()]


blood_group = {

}

occupation = {
    'STUDENT': 'Student',
    'UNEMPLOYED': 'Unemployed',
    'SELF EMPLOYED': 'Self Employed',
    'PUBLIC EMPLOYEE': 'Public Employee',
    'PRIVATE EMPLOYEE': 'Private Employee',
}
occupation_choices = [tuple([v, k]) for k, v in occupation.items()]

category = {
    'GN': 'General',
    'SC': 'Scheduled categorys',
    'ST': 'Scheduled Tribes',
    'OBC': 'Other Backward Classes',
    'SBC': 'Special Backwar Classes',
    'MN': 'Minority',
}
category_choices = [tuple([v, k]) for k, v in category.items()]

maritial_status = {

}
maritial_status_choices = [tuple([v, k]) for k, v in maritial_status.items()]

education_status = {
    'MATRICULATE': '10th Pass',
    'INTERMEDIATE': '12th Pass',
    'GRADUATE': 'Bachelors(1st) Degree',
    'POST GRADUATE': 'Masters(2nd) Degree',
}
education_status_choices = [tuple([v, k]) for k, v in education_status.items()]

income_status = {
    'POOR': 'Earning less than 100K per annum',
    'LOW MIDDLE': 'Earning 100K - 400k per annum',
    'HIGH MIDDLE': 'Earning 400K - 1000K per annum',
    'LOW UPPER': 'Earning 1000K - 1500K per annum',
    'HIGH UPPER': 'Earning more than 1500K per annum',
}
income_status_choices = [tuple([v, k]) for k, v in income_status.items()]

authorization_level = {
    '0': "Entry Level",
    '1': "Mid Level",
    '2': "Senior Level",
    '3': "Super Level",
}
authorization_level_choices = [tuple([v, k]) for k, v in authorization_level.items()]
