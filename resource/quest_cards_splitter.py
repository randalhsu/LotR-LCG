'''Split each W*H quest cards into two H*(W/2) cards, rotated 90 degrees CCW.'''
import glob
import os
from PIL import Image

questCards = {  # EXPANSION
    'core': [
        'a-fork-in-the-road-core',
        'ambush-on-the-shore-core',
        'anduin-passage-core',
        'beorns-path-core',
        'dont-leave-the-path-core',
        'flies-and-spiders-core',
        'out-of-the-dungeons-core',
        'the-necromancers-tower-core',
        'through-the-caverns-core',
        'to-the-river-core',
    ],
    'mirkwood': [
        'against-the-trolls-catc',
        'ambush-rtm',
        'a-new-terror-abroad-thfg',
        'escape-attempt-rtm',
        'grimbeorns-quest-catc',
        'into-the-marshes-tdm',
        'on-the-trail-thfg',
        'radagasts-request-ajtr',
        'return-to-rhosgobel-ajtr',
        'the-capture-tdm',
        'the-hills-of-emyn-muil-thoem',
        'the-hunt-begins-thfg',
        'the-wounded-eagle-ajtr',
        'through-the-forest-rtm',
        'to-the-elven-kings-halls-rtm',
    ],
    'osgiliath': [
        'beyond-expectations-tmao',
        'through-the-ruins-tmao',
        'anduin-crossing-tmao',
        'race-to-minas-tirith-tmao',
    ],
    'khazaddum': [
        'a-presence-in-the-dark-kd',
        'a-way-up-kd',
        'entering-the-mines-kd',
        'goblin-patrol-kd',
        'search-for-an-exit-a-wrong-turn-kd',
        'search-for-an-exit-blocked-by-shadow-kd',
        'search-for-an-exit-escape-from-darkness-kd',
        'search-for-an-exit-hasty-council-kd',
        'search-for-an-exit-heading-down-kd',
        'search-for-an-exit-heading-up-kd',
        'search-for-an-exit-narrow-paths-kd',
        'search-for-the-chamber-kd',
        'the-fate-of-balin-kd',
    ],
    'dwarrowdelf': [
        'up-the-pass-trg',
        'snowdrifts-trg',
        'the-mountains-peaks-trg',
    ],
}

for set_ in questCards:
    for filePath in glob.glob(os.path.join('image', set_, '*.jpg')):
        filePath = filePath[:-4]  # trim '.jpg'
        _, fileName = os.path.split(filePath)
        if fileName in questCards[set_]:
            print(fileName)
            im = Image.open(filePath + '.jpg')
            box = im.getbbox()
            frontBox = (box[0], box[1], box[2], box[3] / 2 - 1)
            print(frontBox)
            front = im.crop(frontBox)
            front = front.rotate(90, Image.BICUBIC, True)
            front.save(filePath + '-A.jpg', 'JPEG', quality=90)
            
            backBox = (box[0], box[3] / 2 - 1, box[2], box[3])
            print(backBox)
            back = im.crop(backBox)
            back = back.rotate(90, Image.BICUBIC, True)
            back.save(filePath + '-B.jpg', 'JPEG', quality=90)
            