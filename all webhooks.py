from discord import Webhook, RequestsWebhookAdapter, Embed, Color



webhook_url = input("请输入你的webhook_url:\n")

print("请选择你的bot：")

bot_select = input("1. Cyber\n2. TKS\n3. Sole\n")



if bot_select == "Cyber":

    product_name = input("请输入你想要的Product名称：\n")

    store_name = input("请输入你想买的store：\n")

    product_size = input("请输入你想要的尺码：\n")

    profile = input("请在|| ||内输入你的profile：\n")

    order_number = input("请在|| ||内输入你的订单号:\n")

    proxy = input("请在|| ||内输入你的proxy：\n")

    product_image = input("请输入商品图片的url：\n")

    def avatar_url():
        return ("https://cdn.discordapp.com/avatars/681870741087584267/5d433280a842a4b5efb8b2e2d63b26cd.webp?size=128")

    def send_webhook():
        url = webhook_url
        webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

        embed = Embed(title="Successfully checked out!", description=product_name,color=Color.from_rgb(115, 238, 139))

        embed.set_thumbnail(url=product_image)

        embed.add_field(name="Store", value=store_name)

        embed.add_field(name="Size", value=product_size)

        embed.add_field(name="Profile", value=profile)

        embed.add_field(name="Order", value=order_number)

        embed.add_field(name="Proxy list", value=proxy)

        embed.add_field(name="mode", value="你猜").set_footer(text="CyberAIO·14/04/2020 10:50:50.263",icon_url="https://cdn.discordapp.com/avatars/681870741087584267/5d433280a842a4b5efb8b2e2d63b26cd.webp?size=128")

        webhook.send(embed=embed, avatar_url=avatar_url(), username="CyberAIO")


    send_webhook()



elif bot_select == "TKS":

    product_name = input("请输入你想要的Product名称：\n")

    store_name = input("请输入你想买的store：\n")

    product_size = input("请在|| ||内输入你想要的尺码：\n")

    product_price = input("请输入商品价格：\n")

    profile = input("请在|| ||内输入你的profile：\n")

    proxy = input("请在|| ||内输入你的proxy：\n")

    product_image = input("请输入商品图片的url：\n")

    def avatar_url():
        return ("https://cdn.discordapp.com/avatars/682088391906558022/eb1ea68a3d2b4f67bc9753a5684353f5.webp?size=128")

    def send_webhook(content):
        url = webhook_url
        webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

        embed = Embed(title="You cooked", color=Color.from_rgb(161, 90, 182))

        embed.set_thumbnail(url=product_image)

        embed.add_field(name="Website", value=store_name)

        embed.add_field(name="Product", value=product_name)

        embed.add_field(name="Size", value=product_size)

        embed.add_field(name="Price", value=product_price)

        embed.add_field(name="Profile", value=profile)

        embed.add_field(name="Proxy", value=proxy)

        embed.add_field(name="Time stamp(utc)", value="2020-04-11 15:08:28PM")

        webhook.send(content, embed=embed, avatar_url=avatar_url(), username="TKS")

    send_webhook(product_name)



elif bot_select == "Sole":

    product_name = input("请输入你想要的Product名称：\n")

    product_size = input("请在|| ||内输入你想要的尺码：\n")

    profile = input("请在|| ||内输入你的profile：\n")

    checkout_time = input("请输入你需要的checkout time：\n")

    monitor_delay = input("请输入你需要的monitor delay：\n")

    retry_delay = input("请输入你需要的retry delay：\n")

    def avatar_url():
        return ("https://media.discordapp.net/attachments/698457195729125447/699465230060879973/image0.jpg?width=300&height=300")

    def send_webhook():
        url = webhook_url

        webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

        embed = Embed(title="Checkout link", url="http://baidu.com", color=Color.from_rgb(115, 238, 139))

        embed.set_image(product_image)

        embed.add_field(name="Product", value=product_name)

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Size", value=product_size)

        embed.add_field(name="Billing Profile", value=profile)

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Checkout Time", value=checkout_time)

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Monitor Delay", value=monitor_delay)

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Retry Delay", value=retry_delay)

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Mode", value="你猜")

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="\u200b", value='\u200b')

        embed.add_field(name="Opinion", value="Pre generated checkout").set_footer(text="Sole AIO Shopify Mode",icon_url="https://media.discordapp.net/attachments/698457195729125447/699465230060879973/image0.jpg?width=300&height=300")

        webhook.send(embed=embed, avatar_url=avatar_url(), username="Sole AIO")

    send_webhook()


