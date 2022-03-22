import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")

    import django
    django.setup()

    from blog import models

    # 基于对象的查询 SQL: 子查询
    # a1 = models.Article.objects.first()
    # print(a1.user.avatar, type(a1.user))
    #
    # # 基于QuerySet查询, SQL: join连表查询
    # a2 = models.Article.objects.filter(pk=1)
    # print(a2.values("user__avatar"))


    # 查询a1对应的评论数
    # ret = models.Article.objects.first().comment_set.all()
    # print(ret)

    # 查询某个分类对应的文章
    from django.db.models import Count
    # user = models.UserInfo.objects.filter(username="qiqi").first()
    # blog = user.blog
    # ret = models.Category.objects.filter(blog=blog)  # 求小黑站点下面所有的文章分类
    # ret = ret[0].article_set.all()  # 技术分类下面所有的文章
    # for i in ret:
    #     print(i.title, i.article_set.all().count())

    # ret = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # print(ret)
    # 基于QuerySet查询的时候 不用加set
    # models.Category.objects.filter(blog=blog).values("article__title")

    # ret = models.Article.objects.filter(user=user).extra(
    #     select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    # ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
    # print(ret)


    # 由 文章表查询 tag表

    ret = models.Article.objects.filter(user=user).filter(tags__title="python")
    print(ret)


