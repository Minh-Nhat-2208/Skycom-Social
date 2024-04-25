import requests, urllib.parse, base64, json, time, re, random, csv, datetime, threading

thread_count = 30
total_changer = 1
program_count = 0

class GroupsProfile():

    def __init__(self):
        # self.api_key = 'a6d5360a023cfc055f59f106aa85af68'
        self.api_key = 'ok82NdXooLIQT1Xg'
        self.total_changer = total_changer
        self.thread_count = thread_count
        self.program_count = program_count
        # self.proxy = {'proxy': 'dangvinhhung:e65FSx6XWMHxWS4@s2.m2proxy.com:8063'}
        self.proxy = {'proxy': 'dangvinhhung:ok82NdXooLIQT1Xg@ip.mproxy.vn:12393'}
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

    def query_group(self, uid_profile):
        node_groups = []
        end_cursor = {'cursor': ''}

        def post_request():

            proxies = {'https': 'http://' + self.proxy['proxy']}

            encoded_bytes = base64.b64encode(str("app_collection:" + uid_profile + ":2361831622:66").encode("utf-8"))
            variables = '{"count":8,"cursor":"' + end_cursor['cursor'] + '","scale":1.5,"search":null,"id":"' + str(encoded_bytes.decode("utf-8")) + '","__relay_internal__pv__VideoPlayerRelayReplaceDashManifestWithPlaylistrelayprovider":false}'
            payload = '&variables=' + urllib.parse.quote_plus(variables) + '&doc_id=8004529446241809k-route-definitions%2F'

            data_response = requests.request("POST", self.url, headers=self.headers, data=payload, timeout=30, proxies=proxies)
            dataJson = json.loads(data_response.text)
            return dataJson

        def regex_groups(dataJson):
            edges = dataJson['data']['node']['pageItems']['edges']
            for item in edges:
                try:
                    count = int(str(item['node']['subtitle_text']['text']).split(" members")[0].replace(",", ""))
                except:
                    count = int(str(item['node']['subtitle_text']['text']).split(" member")[0].replace(",", ""))

                node_gr = {
                    'id': item['node']['node']['id'],
                    'name': item['node']['title']['text'],
                    'visibility': item['node']['node']['privacy_info']['title']['text'],
                    'groups_url': item['node']['url'],
                    'group_member_profiles': {'count': count}
                }
                node_groups.append(node_gr)

        def page_info(dataJson):
            has_next_page = dataJson['data']['node']['pageItems']['page_info']['has_next_page']
            cursor = dataJson['data']['node']['pageItems']['page_info']['end_cursor']
            if has_next_page != True:
                return True
            else:
                end_cursor.update({'cursor': cursor})
                # print(has_next_page, end_cursor)

        while True:
            try:
                dataJson = post_request()
                try:
                    if 'errors' not in dataJson:
                        regex_groups(dataJson)
                        if page_info(dataJson):
                            break
                    else:
                        next_change = random.randint(15, 25)
                        print(
                            f'🚫 Tạm thời không thể requests đến graphql vì bị giới hạn | 🕛 Thử lại sau: {next_change} | {uid_profile}')
                        time.sleep(next_change)
                except Exception as e:
                    print(f'❗ Có lỗi ở phần regex: {e}, {dataJson}')

            except Exception as e:
                next_change = random.randint(15, 25)
                print(f'❗ Có lỗi ở phần requests đến graphql | 🕛 Thử lại sau: {next_change} ')
                time.sleep(next_change)

        return node_groups

    def change_proxy(self, ):
        while True:

            try:
                # rotating_proxy = self.get_rotating_proxy_m2proxy(self.api_key)
                rotating_proxy = self.get_rotating_proxy_mproxy(self.api_key)
                if 'success' in rotating_proxy or str(rotating_proxy['status']) == '1':
                    print(f'🌐 Changer Proxy Success: {self.proxy}')
                    time.sleep(80)
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

        thread_a = threading.Thread(target=self.change_proxy)
        thread_a.start()
        time.sleep(5)

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
                basic_info = check_live_profile(uid_profile, self.proxy)
                if basic_info is not None:
                    node_groups = self.query_group(uid_profile)
                    groupsDB = {"person_uid": str(uid_profile), "data": node_groups}
                    # connectDB.insert_groups(groupsDB)

                    add_data_groups(groupsDB)
                    update_count_groups(groupsDB)

                    print(f'🟢 Crawl UID Success: {self.program_count, self.proxy["proxy"], groupsDB["person_uid"], len(groupsDB["data"])}')
                    self.program_count += 1

                else:
                    item_data = {'person_uid': uid_profile, "data": [], 'feedback': 'Nguời Dùng Không Tồn Tại'}
                    add_data_groups(item_data)
                    update_count_groups(item_data)
                    print(f'🔴 Account không tồn tại: {uid_profile}')

            except Exception as e:
                print(f'⚠️ Error: {e}')
                time.sleep(random.randint(8, 15))
                main_app(uid_profile)

        def check_live_profile(uid_profile, proxy):
            url = f"https://graph.facebook.com/{uid_profile}/picture?type=normal"
            r = requests.get(url, proxies=proxy)

            if "100x100" in str(r.url):
                return True

        def get_uid_profile():
            url = 'http://skycom.ddns.net/profile/overview/get_person_uid_next_crawl_groups'
            response = requests.request("GET", url).json()
            return response['data'][0]['person_uid']

        def check_uid_profile(uid_profile):
            url = f'http://skycom.ddns.net/groups/list?profile_id={uid_profile}'
            response = requests.request("GET", url).json()
            return response

        def update_count_groups(dataGroupsJson):
            url = f'http://skycom.ddns.net/profile/overview/update_groups_counts'
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=json.dumps(dataGroupsJson)).json()
            return response

        def add_data_groups(dataGroupsJson):
            url = f'http://skycom.ddns.net/groups/add'
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
                    # Update count groups to overview
                    response = update_count_groups(dataGroupsJson)
                    print(f'🟡 Account đã được crawl trước đó: {uid_profile} >> 🟡 {response["message"]}')
            except Exception as e:
                print(f'⚠️ Error: {e}')


if __name__ == '__main__':
    GroupsProfile().start_program()
