from flet import *


def main(page: Page):
    page.bgcolor = "#2e515d"   # 6 خانات = لون صلب

    # AppBar بيتحط في page.appbar مباشرة
    page.appbar = AppBar(
        actions=[
            IconButton(
                icon=Icons.SUNNY,
                tooltip="تبديل الوضع",
            )
        ],
        actions_padding=Padding.all(10),
        bgcolor="#f0205d",       # 6 خانات
        center_title=True,
        color="#ffffff",         # لون النص والأيقونات
        title=Text("Ahmed gamel"),
    )

    # SafeArea بتحمي المحتوى (body) من النوتش
    page.add(
        SafeArea(
            expand=True,
            content=Column(
                controls=[
                    Text("محتوى التطبيق هنا", color="white", size=20),
                ]
            ),
        )
    )


run(main)
