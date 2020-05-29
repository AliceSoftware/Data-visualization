from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    """根据指定的国家,返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif 'Yemen, Rep.' == country_name:
            return 'ye'
        elif 'Vietnam' == country_name:
            return 'vn'
        elif 'Korea, Dem. Rep.' == country_name:
            return 'kp'
        elif 'Korea, Rep.' == country_name:
            return 'kr'
        elif 'Egypt, Arab Rep.' == country_name:
            return 'eg'
        elif 'Bolivia' == country_name:
            return 'bo'
        elif 'Congo, Dem. Rep.' == country_name:
            return 'cd'
        elif 'Congo, Rep.' == country_name:
            return 'cg'
        elif 'Gambia, The' == country_name:
            return 'gm'
        elif 'Iran, Islamic Rep.' == country_name:
            return 'ir'
        elif 'Dominica' == country_name:
            return 'do'
        elif 'Kyrgyz Republic' == country_name:
            return 'kg'
        elif 'Tanzania' == country_name:
            return 'tz'
        elif 'Venezuela, RB' == country_name:
            return 've'
        elif 'Slovak Republic' == country_name:
            return 'sk'
        elif 'Lao PDR' == country_name:
            return 'la'
    # 如果没有找到指定的国家,就返回None
    return None
