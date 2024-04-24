import requests, urllib.parse, base64, json, time, re, random, csv, datetime, threading

thread_count = 20
total_changer = 1
program_count = 0

class AboutsProfile():

    def __init__(self):
        self.api_key = 'a1abe169f522007f2ca4b84157d764a0'
        self.total_changer = total_changer
        self.thread_count = thread_count
        self.program_count = program_count
        self.proxy = {'proxy': 'dangvinhhung:e65FSx6XWMHxWS4@s2.m2proxy.com:8832'}
        self.url = 'https://www.facebook.com/api/graphql/'
        self.headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '',
            'dpr': '1.125',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
            'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.129", "Not(A:Brand";v="24.0.0.0", "Microsoft Edge";v="122.0.2365.92"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
            'viewport-width': '980',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'ProfileCometAppCollectionListRendererPaginationQuery',
            'Connection': 'close'
        }

    def about_overview(self, uid_profile):

        aboutOverview = {'person_uid': uid_profile}

        def post_request_api():

            proxies = {'https': 'http://' + self.proxy['proxy']}

            encoded_bytes = base64.b64encode(str("app_section:" + uid_profile + ":2327158227").encode("utf-8"))
            variables = '{"appSectionFeedKey":"ProfileCometAppSectionFeed_timeline_nav_app_sections__' + uid_profile + ':2327158227","collectionToken":null,"pageID":"' + uid_profile + '","rawSectionToken":"' + uid_profile + ':2327158227","scale":1,"sectionToken":"' + str(encoded_bytes.decode("utf-8")) + '","showReactions":true,"userID":"' + uid_profile + '","__relay_internal__pv__VideoPlayerRelayReplaceDashManifestWithPlaylistrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}'

            payload = ('av=0&__aaid=0&__user=0&__a=1&__req=i&__hs=19809.HYP%3Acomet_loggedout_pkg.2.1..0.0&dpr=1&__ccg'
                       '=EXCELLENT&__rev=1012348741&__s=9w8b6t%3Aezmuan%3A5f4jpa&__hsi=7351042330832115203&__dyn'
                       '=7xeUmwlEnwn8yEqxemh0cm5U4e1Nxt3odEc8co5S3O2Saw8i2S1DwUx60gu0luq1ew65xO2OU7m0yE462mcwfG12wOx62G3i0Bo7O2l0Fwqo31w9O7Udo5qfK0zEkxe2Gewywuo88brwKxm5odK1lUlDw-waCm7-0gq2i2S3qazo3iwPwbS16xi4UdUcobUak0KU566E6C13G1-wkEaEdouw&__csr=g9cAug_sIJFFitfGWt4bmtLgKG_hABiAZqQmCJeRiJFuWBJbGAH8F6qniGnAKF9by8y9F5CWDCCyVpp9UKazayeWWAu9Vpuu9CLpSHCgV5GvUSLyqzFet2UgUl-cG58W9hUSqmclpvyHUDhXVeRDK8Agy_AAwSKm9GUGEBauq9xe3yV8WaAKJ2E0T20tO5E2Nwd22-0m9wmo1w4Eeo3Nw1021Mw4Ew29o0zW0kwE0S-0f1w7ug423u2K0yS0uVxe2V0NzP02ko2axC02xeh0cDpoB01ewE0zoc2UB1wak03LKt01s10aV0l80t5w1aC06Fo3wwso1We3h0hu1wwzcewq417g72tPwdi0st0Txy1pCw4iJ0aO6Ea84qhwbm13w52xe0D9Qu0gW4odo5K1fx20D4QK2WqkyDwcO0gt0gQ0U40oq0-U2_w8Gt02mEGq4u5FiNaxl1zhEqzU2ZFfUG2R0MgVwhEC4U1r26GucwOw5dy81qO4G2mtU3HAwiQ8dg3eyo-hwCEFK1PyEO8w4awWwDw7pgC2y0S8ng4JCyInkHwIobT4NaOTh5wxp82Sz88UjwzwcVDykcy82ko2Fo4arkiElh9EOU6Ew6e0guVQ0cExl1zoeA6E08K8ixTw2uV6ewi86O0Lo2IwCg1K81lFA482mojwJw4Y53TQyBy-8DUW0HUiwl82Dw4Cwk20nlwddw2a8eEkyE2vgey0nEdUZwdc5UoODwVw5swtU4C9m9QU1lVS2a3y2y2i3MyiyoSkE25S0c5Q0lqA0tcw3Ww&__comet_req=15&lsd=AVoWAbpQ1Sg&jazoest=2940&__spin_r=1012348741&__spin_b=trunk&__spin_t=1711547917&fb_api_caller_class='
                       'RelayModern&fb_api_req_friendly_name=ProfileCometAboutAppSectionQuery&variables=') + urllib.parse.quote_plus(variables) + '&doc_id=7146363115461401'

            data_response = requests.request("POST", self.url, headers=self.headers, data=payload, proxies=proxies, timeout=30)

            return data_response.text.split('\n')[0]

        def post_request_url():
            node_about = []
            session = self.profile_session()
            session.proxies = {'https': 'http://' + self.proxy['proxy']}

            url = f"https://www.facebook.com/{uid_profile}"
            data_response = session.request("GET", url, timeout=20)

            edges = re.findall(r'data-sjs>([^<]+)', data_response.text)

            for item in edges:
                if str(item).find("profile_field_sections") > 10:
                    jsonItem = json.loads(item)

                    result = jsonItem['require'][0][3][0]['__bbox']['require']

                    for style_renderer in result:
                        if str(style_renderer).find("profile_field_sections") > 10:

                            field_sections = style_renderer[3][1]['__bbox']['result']['data']['style_renderer'][
                                'profile_field_sections']

                            for sections in field_sections:
                                for title in sections['profile_fields']['nodes']:

                                    if "to show" not in str(title['title']['text']):
                                        item = {sections['title']['text'].lower().replace(' ', '_'): title['title']['text']}
                                        node_about.append(item)

            return node_about

        def regex_about_overview(data_response):

            dataJson = json.loads(data_response)

            if not dataJson['data']['user']:
                print(f'⚠️ Account không tồn tại: {uid_profile}')

            elif not dataJson['data']['user']['about_app_sections']['nodes']:
                # print("No nodes found", "Thực hiện lấy thông tin bằng cách 2")
                node_about = post_request_url()
                for node in node_about:
                    aboutOverview.update(node)

            else:
                nodes = dataJson['data']['user']['about_app_sections']['nodes']
                activeCollections = nodes[0]['activeCollections']['nodes'][0]['style_renderer']['profile_field_sections'][0]['profile_fields']['nodes']

                for node in activeCollections:
                    if 'null_state' not in node['field_type']:

                        if node['renderer']['field']['text_content'] is None:
                            item = {node['field_type']: node['renderer']['field']['title']['text']}
                        else:
                            item = {node['field_type']: node['renderer']['field']['text_content']['text']}
                        aboutOverview.update(item)

        response = post_request_api()
        regex_about_overview(response)
        return aboutOverview

    def profile_field_person(self, uid_profile):
        session = requests.session()
        session.proxies = {'https': 'http://' + self.proxy['proxy']}

        session.headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="121.0.2277.83", "Chromium";v="121.0.6167.85"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'viewport-width': '1195',
            'Cookie': '',
            'Connection': 'close'
        }

        url = f"https://www.facebook.com/marketplace/profile/{uid_profile}"
        response = session.request("GET", url, timeout=20)

        edges = re.findall(r'data-sjs>([^<]+)', response.text)

        for item in edges:
            if item.find("marketplace_user_profile") > 10:
                jsonItem = json.loads(item)

                try:

                    user = jsonItem['require'][0][3][0]['__bbox']['require'][3][3][1]['__bbox']['result']['data'][
                        'user']
                except:
                    user = jsonItem['require'][0][3][0]['__bbox']['require'][0][3][1]['__bbox']['result']['data'][
                        'user']

                try:
                    person_current_city = user['items']['nodes'][0]['title']['text']
                except:
                    person_current_city = None

                if "people" in str(user['url']):
                    friend_url = f'https://www.facebook.com/{uid_profile}'
                else:
                    friend_url = user['url']

                basic_info = {
                    'name': user['name'],
                    'gender': user['gender'],
                    'current_city': person_current_city,
                    'url': friend_url,
                }
                return basic_info

    def profile_session(self, ):

        session = requests.session()
        session.headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="121.0.2277.83", "Chromium";v="121.0.6167.85"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'viewport-width': '1195',
            'Cookie': '',
            'Connection': 'close'
        }

        return session

    def change_proxy(self, ):
        while True:

            try:
                # rotating_proxy = self.get_rotating_proxy_m2proxy(self.api_key)
                rotating_proxy = self.get_rotating_proxy_mproxy(self.api_key)
                if 'success' in rotating_proxy or str(rotating_proxy['status']) == '1':
                    print(f'🌐 Changer Proxy Success: {self.proxy}')
                    time.sleep(50)
                else:
                    try:
                        next_change = re.findall(r"\d+", rotating_proxy['Message'])
                    except:
                        next_change = rotating_proxy["data"]["remaining_time"]

                    if next_change:
                        time.sleep(int(next_change))
                    else:
                        time.sleep(10)
            except:
                time.sleep(10)

    def get_rotating_proxy_m2proxy(self, api_key):
        url = f'https://api.m2proxy.com/user/package/changeip?package_api_key={api_key}'
        response = requests.request("GET", url).json()
        return response
    def get_rotating_proxy_mproxy(self, api_key):
        url = f'https://mproxy.vn/capi/OV4Mt7wJ5zUZfkWW765MzDLDXIxtPhUN2q9Xx8UIrhk/key/{api_key}/resetIp'
        response = requests.request("GET", url).json()
        return response

    def start_program(self):

        # thread_a = threading.Thread(target=self.change_proxy)
        # thread_a.start()
        # time.sleep(5)

        while True:
            if self.proxy['proxy'] != None:

                for thread_step in range(0, thread_count):
                    new_thread = threading.Thread(target=self.main, args={thread_step, })
                    time.sleep(random.randint(1, 10000) / 10000)
                    new_thread.start()
                break

    def main(self, thread_step):

        def main_app(uid_profile):
            try:
                basic_info = self.profile_field_person(uid_profile)
                if basic_info is not None:
                    aboutOverview = self.about_overview(uid_profile)
                    aboutOverview.update(basic_info)

                    add_data_abouts(aboutOverview)
                    update_status_abouts(aboutOverview)

                    print(f'🟢 Crawl UID Success: {self.program_count, self.proxy["proxy"], aboutOverview["person_uid"], aboutOverview["name"], aboutOverview["gender"]}')
                    self.program_count += 1

                else:
                    item_data = {'person_uid': uid_profile, 'feedback': 'Nguời Dùng Không Tồn Tại', 'status': 'die'}
                    add_data_abouts(item_data)
                    update_status_abouts(item_data)
                    print(f'🔴 Account không tồn tại: {uid_profile}')

            except Exception as e:
                print(f'⭕ Error: {e}')
                time.sleep(random.randint(8, 15))
                main_app(uid_profile)


        def get_uid_profile():
            url = 'http://skycom.ddns.net/profile/overview/get_person_uid_next_crawl_abouts'
            response = requests.request("GET", url).json()
            return response['data'][0]['person_uid']

        def check_uid_profile(uid_profile):
            url = f'http://skycom.ddns.net/profile/account?id={uid_profile}'
            response = requests.request("GET", url).json()
            return response

        def update_status_abouts(dataGroupsJson):
            url = f'http://skycom.ddns.net/profile/overview/update_profile_abouts'
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=json.dumps(dataGroupsJson)).json()
            return response

        def add_data_abouts(dataGroupsJson):
            url = f'http://skycom.ddns.net/profile/add'
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=json.dumps(dataGroupsJson)).json()
            return response

        while True:
            try:
                # Lấy profile ID
                uid_profile = get_uid_profile()

                # Check xem profile đã craw trước đó chưa
                dataGroupsJson = check_uid_profile(uid_profile)
                if not dataGroupsJson['data']:
                    main_app(uid_profile)
                else:
                    # Update status profile to overview
                    response = update_status_abouts(dataGroupsJson)
                    print(f'🟡 Account đã được crawl trước đó: {uid_profile} >> 🟡 {response["message"]}')
            except Exception as e:
                print(f'⚠️ Error: {e}')


if __name__ == '__main__':
    AboutsProfile().start_program()
