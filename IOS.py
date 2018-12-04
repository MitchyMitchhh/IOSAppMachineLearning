# Test
data = "appleStore_description.csv"
file = pd.read_csv(data, delim_whitespace=True)
file.columns = ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver',
                'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num',
                'ipadSc_urls.num', 'lang.num', 'vpp_lic', 'game_enab']