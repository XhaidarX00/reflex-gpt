import requests

headers = {
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'X-Same-Domain': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua-full-version': '"128.0.6613.138"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'Referer': 'https://gemini.google.com/',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.138", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.138"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'bl': 'boq_assistant-bard-web-server_20240911.02_p1',
    'f.sid': '1983574883511299981',
    'hl': 'id',
    '_reqid': '1685330',
    'rt': 'c',
}

data = 'f.req=%5Bnull%2C%22%5B%5B%5C%22menggunakan%20gemini%20apakah%20ada%20limit%20harian%20permintaan%20untuk%20akun%20saya%3F%2C%20jika%20iya%20berapa%20maksimal%20limit%20harian%3F%5C%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C0%5D%2C%5B%5C%22id%5C%22%5D%2C%5B%5C%22%5C%22%2C%5C%22%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22%5C%22%5D%2C%5C%22!ODulO2PNAAb6zjAV2s5CPlsfGNoh2207ADQBEArZ1ORMz2zP3nDegySRY3CUkrHn8zVIMG4GkhxLjXOEdP1UjS6ui3r8n-_qdPS9vCFdAgAAAJpSAAAAB2gBB34AQDSJ5V-1eBX-zfVSFmdbhrA31YCEr8xPGzNatIhBd3ZkAJ8GQAre4bBTxPij3fUmAjum8Kq18xpQrRYX3FeM0CSZAwGvTc3D1d_T8a1b7B43n1BDc0vpbbHATTAThOnAc-Ts5_7QrZfkJEKHpZAgi-q5dGAZCdti-Uq6SXsjmqQX2fSX2_v2miIQS7TFq02_-0MN_H7HO5h9Eki-8EEZE12tML54P5v1D3vBAhXvVjPXRVVwwJvAp8f3_XnP4UiUWHtUtAOTCu0-08BPufajk08u4FnX8yDA-tpCBGrqbvYgDNtA3jM3qRpCvgqLMdH3oL5GDwcUjLtKJLHJhfxX0_mcFFqyodhDAlDyTAVcC48SxcZtFO7USw9xnyr_7RE2xHYul4D_LI4bH05lYQ-WZnbu0Nyp5OJWel-gN-6KjWTw4Uq9dVzgNhBy3_trlx0ITlEnLqfVwf_G8qSXW7Xj297Y5QcWBALH4F6SEU-dFBUSKUIApUC3cUk_1GkaREA9QcstBAX73Ix6AgVuLd2dU9khWNMHhcEqKBPR6rkvfKkf9mViPAEpq16pdW9EKZg6HBfWuWNj21wnoFgSdNmlc0D6dwC-4rnG7dKWZliNvEKxjkgT0qQOXbnWuH1PxBQKkoeAOGghhys0g7U44xnJSajDBC9KJ1SoAIkWmokAiXM9LHeRzEt5tZ2hjVUKDGpXGcK18w1SFmx_pZkD31-XZysFabj_rL8U3unmODOuM2pRzVkUryDz8s0zm349oztP7MopdgshmtC_iUKvkO-DrrgESvb9jg0UxQgSNYwBWIVnWHLwiAgaT3Y4PF6KilWfdGzoKQ9z6cFw-kP2azVxLIOZoiP0ZV2t0Hh-03R0L9xlCXkjiBOqa2DCbBX-B8KKv0_KssLn8Yvw0dz5tpmH_bqNsHukR2VwXXW51PIgSGl_FaL4kveezxmIchmGhyvsjGL1d-TKnOlpewYTfVU_tZ4QdznL8QAjvY015LZ6o0Lpl6EdUEwsyADip2VNIEe3sIiSOvZFQRlux_baXWYZV7B8NnX9uGG6YJzAOlPwXsxMPCQDcV9KQtP9GFuPquVXPE856Qd65CjcUWY4Njfr4h_9-xqY%5C%22%2C%5C%22b7c92318b8b216a02b7ad6e338167e30%5C%22%2Cnull%2C%5B1%5D%2C1%2Cnull%2Cnull%2C1%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2C%5B%5B0%5D%5D%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%22%5D&at=AGowkknJOEPavU9-A9Yl4P9v1-Hp%3A1726245728512&'

response = requests.post(
    'https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
    params=params,
    headers=headers,
    data=data,
)