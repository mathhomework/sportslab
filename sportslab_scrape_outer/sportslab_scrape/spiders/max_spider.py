from scrapy.spider import Spider
from scrapy.selector import Selector

# example curl
#curl http://localhost:6800/schedule.json -d project=sportslab_scrape -d spider=max -d max_url="http://www.maxpreps.com/high-schools/de-la-salle-spartans-(concord,ca)/football/stats.htm"

#example terminal crawl
# scrapy crawl max -a max_url="http://www.maxpreps.com/high-schools/de-la-salle-spartans-(concord,ca)/football/stats.htm"
from sportslab_scrape.items import PassingItem, RushingItem, ReceivingItem


class MaxSpider(Spider):
    name = "max"

    def __init__(self, max_url=None, *args, **kwargs):
        super(MaxSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["{}".format(max_url)]

    allowed_domains = ['maxpreps.com']
    start_urls = [
        # "http://www.maxpreps.com/high-schools/de-la-salle-spartans-(concord,ca)/football/stats.htm"
    ]

    def parse(self, response):
        sel = Selector(response)
        school = sel.xpath("//ul[@id='breadcrumb']/li[last()-1]/a/span/text()").extract()[0]
        print school
        passing = sel.xpath("//h3[@id='offense_passing']/following-sibling::table[1]")
        passing_players = passing.xpath("tbody/tr/.//text()[parent::a|parent::td]").extract()
        # test = [td.xpath(".//text()").extract() or [u'Null'] for Selector in rushing.xpath("tbody/tr/td[@class='rushinglong stat dw']")]
        # test2 = [td.xpath(".//text()").extract() or '' for td in passing.xpath("tbody/tr/.//text()[parent::a|parent::td]")]
        # test5 = [''.join(td.xpath('.//text()').extract()) for td in passing.xpath('tbody/tr/td[@class="ydspercompletion stat dw"]')]
        passing_players_stats = [''.join(td.xpath('.//text()').extract()) for td in passing.xpath('tbody/tr/td')]
        passing_players_names = passing.xpath('tbody/tr/th/a/@title').extract()

        passing_players_stats_cat = passing.xpath("thead/tr/th[not(@class=' name string')]/a/text()").extract()
        passing_players_names_cat = passing.xpath("thead/tr/th[@class=' name string']/a/text()").extract()

        rushing = sel.xpath("//h3[@id='offense_rushing']/following-sibling::table[1]")
        rushing_players = rushing.xpath("tbody/tr/.//text()[parent::a|parent::td]").extract()
        rushing_players_stats = [''.join(td.xpath('.//text()').extract()) for td in rushing.xpath('tbody/tr/td')]
        rushing_players_names = rushing.xpath('tbody/tr/th/a/@title').extract()

        rushing_players_stats_cat = rushing.xpath("thead/tr/th[not(@class=' name string')]/a/text()").extract()
        rushing_players_names_cat = rushing.xpath("thead/tr/th[@class=' name string']/a/text()")

        receiving = sel.xpath("//h3[@id='offense_receiving']/following-sibling::table[1]")
        receiving_players = receiving.xpath("tbody/tr/.//text()[parent::a|parent::td]").extract()
        receiving_players_stats = [''.join(td.xpath('.//text()').extract()) for td in receiving.xpath('tbody/tr/td')]
        receiving_players_names = receiving.xpath('tbody/tr/th/a/@title').extract()

        receiving_players_stats_cat = receiving.xpath("thead/tr/th[not(@class=' name string')]/a/text()").extract()
        receiving_players_names_cat = receiving.xpath("thead/tr/th[@class=' name string']/a/text()").extract()
        # print passing_players_stats
        # print passing_players_names
        # print len(passing_players_stats_cat)
        # print passing_players_names_cat
        passing_dict = {}
        passing_end_num = len(passing_players_stats)/len(passing_players_names)
        print passing_players_names_cat
        for name in passing_players_names:
            passing_dict[name] = {passing_players_names_cat[0]: name}
            passing_dict[name].update(dict(zip(passing_players_stats_cat, passing_players_stats[0:len(passing_players_stats_cat)])))
            # print passing_dict[name]
            p = PassingItem()
            p["category"] = u'Passing'
            p["jersey_number"] = passing_dict[name]["#"]
            p["athlete_name"] = name
            p["school"] = school
            p["games_played"] = passing_dict[name]["GP"]
            p["passing_comp"] = passing_dict[name]["C"]
            p["passing_att"] = passing_dict[name]["Att"]
            p["passing_yards"] = passing_dict[name]["Yds"]
            p["completion_percentage"] = passing_dict[name]["C%"]
            p["yds_per_completion"] = passing_dict[name]["Avg"]
            p["passing_yards_per_game"] = passing_dict[name]["Y/G"]
            p["completions_per_game"] = passing_dict[name]["C/G"]
            p["passing_td"] = passing_dict[name]["TD"]
            p["passing_tds_per_game"] = passing_dict[name]["TD/G"]
            p["passing_int"] = passing_dict[name]["Int"]
            p["passing_long"] = passing_dict[name]["Lng"]
            p["qb_rating"] = passing_dict[name]["QB Rate"]
            yield p
            del passing_players_stats[0:passing_end_num]


        rushing_dict = {}
        rushing_end_num = len(rushing_players_stats)/len(rushing_players_names)
        for name in rushing_players_names:
            rushing_dict[name] = {rushing_players_names_cat[0]: name}
            rushing_dict[name].update(dict(zip(rushing_players_stats_cat, rushing_players_stats[0:len(rushing_players_stats_cat)])))
            r = RushingItem()
            r["category"] = u'Rushing'
            r["jersey_number"] = rushing_dict[name]["#"]
            r["athlete_name"] = name
            r["school"] = school
            r["games_played"] = rushing_dict[name]["GP"]
            r["rushing_num"] = rushing_dict[name]["Car"]
            r["rushing_yards"] = rushing_dict[name]["Yds"]
            r["yards_per_carry"] = rushing_dict[name]["Avg"]
            r["rushing_yards_per_game"] = rushing_dict[name]["Y/G"]
            r["rushing_long"] = rushing_dict[name]["Lng"]
            r["rushing_onehundredplus"] = rushing_dict[name]["100+"]
            r["rushing_tdnum"] = rushing_dict[name]["TD"]
            yield r
            del rushing_players_stats[0:rushing_end_num]

        receiving_dict = {}
        receiving_end_num = len(receiving_players_stats)/len(receiving_players_names)
        print receiving_players_names_cat
        for name in receiving_players_names:
            receiving_dict[name] = {receiving_players_names_cat[0]: name}
            receiving_dict[name].update(dict(zip(receiving_players_stats_cat, receiving_players_stats[0:len(receiving_players_stats_cat)])))
            p = ReceivingItem()
            p["category"] = u'Receiving'
            p["jersey_number"] = receiving_dict[name]["#"]
            p["athlete_name"] = name
            p["school"] = school
            p["games_played"] = receiving_dict[name]["GP"]
            p["receiving_num"] = receiving_dict[name]["Rec"]
            p["receiving_yards"] = receiving_dict[name]["Yds"]
            p["yards_per_catch"] = receiving_dict[name]["Avg"]
            p["receiving_yards_per_game"] = receiving_dict[name]["Y/G"]
            p["receiving_long"] = receiving_dict[name]["Lng"]
            p["receiving_tdnum"] = receiving_dict[name]["TD"]
            yield p
            del receiving_players_stats[0:receiving_end_num]
