import calendar

from django.http import Http404
from datetime import datetime, date
from calendar import monthrange

def get_dict_index_from_list(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def get_value_or_404(dict_, key):
    try:
        return dict_[key]
    except Exception as e:
        print str(e)
        raise Http404(str(e))

def get_value_or_default(dict_, key, default=None):
    try:
        ret = dict_[key]
    except:
        ret = default
    return ret

def get_boolean(boolean_str):
    ret = True if boolean_str == 'true' else False
    return ret

def get_date_obj(date_str):
    ret = datetime.strptime(date_str, "%Y-%m-%d").date()
    return ret

def get_date_str(year, month, day):
    ret = date(year, month, day).strftime('%Y-%m-%d')
    return ret

def get_current_year():
    year = int(datetime.now().year)
    return year

def get_current_month():
    month = int(datetime.now().month)
    return month

def get_current_day():
    day = int(datetime.now().day)
    return day

def get_month_name(month):
    month_name = calendar.month_name[month]
    return month_name

def get_month_total_days(year, month):
    total_days = int(monthrange(year, month)[1])
    return total_days

def get_countries():
    countries_str = 'Afghanistan,93/Albania,355/Algeria,213/American Samoa,1684/Andorra,376/Angola,244/Anguilla,1264/Antarctica,672/Antigua and Barbuda,1268/Argentina,54/Armenia,374/Aruba,297/Australia,61/Austria,43/Azerbaijan,994/Bahamas,1242/Bahrain,973/Bangladesh,880/Barbados,1246/Belarus,375/Belgium,32/Belize,501/Benin,229/Bermuda,1441/Bhutan,975/Bolivia,591/Bosnia and Herzegovina,387/Botswana,267/Brazil,55/British Indian Ocean Territory,246/British Virgin Islands,1284/Brunei,673/Bulgaria,359/Burkina Faso,226/Burundi,257/Cambodia,855/Cameroon,237/Canada,1/Cape Verde,238/Cayman Islands,1345/Central African Republic,236/Chad,235/Chile,56/China,86/Christmas Island,61/Cocos Islands,61/Colombia,57/Comoros,269/Cook Islands,682/Costa Rica,506/Croatia,385/Cuba,53/Curacao,599/Cyprus,357/Czech Republic,420/Democratic Republic of the Congo,243/Denmark,45/Djibouti,253/Dominica,1767/Dominican Republic,1809/East Timor,670/Ecuador,593/Egypt,20/El Salvador,503/Equatorial Guinea,240/Eritrea,291/Estonia,372/Ethiopia,251/Falkland Islands,500/Faroe Islands,298/Fiji,679/Finland,358/France,33/French Polynesia,689/Gabon,241/Gambia,220/Georgia,995/Germany,49/Ghana,233/Gibraltar,350/Greece,30/Greenland,299/Grenada,1473/Guam,1671/Guatemala,502/Guernsey,441481/Guinea,224/GuineaBissau,245/Guyana,592/Haiti,509/Honduras,504/Hong Kong,852/Hungary,36/Iceland,354/India,91/Indonesia,62/Iran,98/Iraq,964/Ireland,353/Isle of Man,441624/Israel,972/Italy,39/Ivory Coast,225/Jamaica,1876/Japan,81/Jersey,441534/Jordan,962/Kazakhstan,7/Kenya,254/Kiribati,686/Kosovo,383/Kuwait,965/Kyrgyzstan,996/Laos,856/Latvia,371/Lebanon,961/Lesotho,266/Liberia,231/Libya,218/Liechtenstein,423/Lithuania,370/Luxembourg,352/Macau,853/Macedonia,389/Madagascar,261/Malawi,265/Malaysia,60/Maldives,960/Mali,223/Malta,356/Marshall Islands,692/Mauritania,222/Mauritius,230/Mayotte,262/Mexico,52/Micronesia,691/Moldova,373/Monaco,377/Mongolia,976/Montenegro,382/Montserrat,1664/Morocco,212/Mozambique,258/Myanmar,95/Namibia,264/Nauru,674/Nepal,977/Netherlands,31/Netherlands Antilles,599/New Caledonia,687/New Zealand,64/Nicaragua,505/Niger,227/Nigeria,234/Niue,683/North Korea,850/Northern Mariana Islands,1670/Norway,47/Oman,968/Pakistan,92/Palau,680/Palestine,970/Panama,507/Papua New Guinea,675/Paraguay,595/Peru,51/Philippines,63/Pitcairn,64/Poland,48/Portugal,351/Puerto Rico,1787/Qatar,974/Republic of the Congo,242/Reunion,262/Romania,40/Russia,7/Rwanda,250/Saint Barthelemy,590/Saint Helena,290/Saint Kitts and Nevis,1869/Saint Lucia,1758/Saint Martin,590/Saint Pierre and Miquelon,508/Saint Vincent and the Grenadines,1784/Samoa,685/San Marino,378/Sao Tome and Principe,239/Saudi Arabia,966/Senegal,221/Serbia,381/Seychelles,248/Sierra Leone,232/Singapore,65/Sint Maarten,1721/Slovakia,421/Slovenia,386/Solomon Islands,677/Somalia,252/South Africa,27/South Korea,82/South Sudan,211/Spain,34/Sri Lanka,94/Sudan,249/Suriname,597/Svalbard and Jan Mayen,47/Swaziland,268/Sweden,46/Switzerland,41/Syria,963/Taiwan,886/Tajikistan,992/Tanzania,255/Thailand,66/Togo,228/Tokelau,690/Tonga,676/Trinidad and Tobago,1868/Tunisia,216/Turkey,90/Turkmenistan,993/Turks and Caicos Islands,1649/Tuvalu,688/U.S. Virgin Islands,1340/Uganda,256/Ukraine,380/United Arab Emirates,971/United Kingdom,44/United States,1/Uruguay,598/Uzbekistan,998/Vanuatu,678/Vatican,379/Venezuela,58/Vietnam,84/Wallis and Futuna,681/Western Sahara,212/Yemen,967/Zambia,260/Zimbabwe,263'
    countries_list = []
    countries = countries_str.split('/')
    for country in countries:
        country_list = country.split(',')
        country_obj = {'name': country_list[0].upper(), 'code': int(country_list[1])}
        countries_list.append(country_obj)
    return countries_list
