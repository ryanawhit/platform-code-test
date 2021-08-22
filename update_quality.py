def update_quality(awards):
    updater = QualityUpdater()
    for award in awards:
        if award.name == "Blue First":
            updater.update_blue_first(award)
        elif award.name == "Blue Compare":
            updater.update_blue_compare(award)
        elif award.name == "Blue Star":
            updater.update_blue_star(award)
        elif award.name.startswith("NORMAL"):
            updater.update_normal(award)


class QualityUpdater:
    def update_blue_star(self, award):
        if award.quality > 0:
            award.quality -= 2
        award.expires_in -= 1
        if award.expires_in < 0:
            if award.quality > 0:
                award.quality -= 2
        if award.quality < 0:
            award.quality = 0

    def update_blue_first(self, award):
        if award.quality < 50:
            award.quality += 1           
        award.expires_in -= 1
        if award.expires_in < 0:
            if award.quality < 50:
                award.quality += 1

    def update_blue_compare(self, award):
        if award.quality < 50:
            award.quality += 1
        if award.expires_in < 11:
            if award.quality < 50:
                award.quality += 1
        if award.expires_in < 6:
            if award.quality < 50:
                award.quality += 1               
        award.expires_in -= 1
        if award.expires_in < 0:
            award.quality = award.quality - award.quality

    def update_normal(self, award):
        if award.quality > 0:
            award.quality -= 1
        award.expires_in -= 1      
        if award.expires_in < 0:
            if award.quality > 0:
                award.quality -= 1
