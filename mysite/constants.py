days_of_the_week = {
    'Monday': 'Monday',
    'Tuesday': 'Tuesday',
    'Wednesday': 'Wednesday',
    'Thursday': 'Thursday',
    'Friday': 'Friday',
    'Saturday': 'Saturday',
    'Sunday': 'Sunday',
}
days_of_the_week_choices = [tuple([v, k]) for k, v in days_of_the_week.items()]

language = {
    'hi': 'Hindi',
    'en-uk': 'English UK',
    'en-usa': 'English USA'
}
language_choices = [tuple([v, k]) for k, v in language.items()]


states_in_india = {
    'AN': 'Andaman and Nicobar Islands',
    'AP': 'Andhra Pradesh',
}
states_in_india_choices = [tuple([v, k]) for k, v in states_in_india.items()]
