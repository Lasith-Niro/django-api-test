
# python manage.py shell


from story.models import Story

s1 = Story(title="Harry Potter: Magical Creatures Coloring Book",
            content="House-elves and merpeople, Cornish pixies and dragons--the wizarding world is populated by an unforgettable cast of magical beings and extraordinary beasts. Filled with detailed illustrations inspired by the Harry Potter films, this coloring book presents the creatures of the Forbidden Forest, the Great Lake, and much more. Relive favorite scenes like Harry, Ron, and Hermione's escape from Gringotts on the back of a dragon and explore intricate creature-themed patterns in this interactive journey through the wizarding world.",
            rating=4)

s2=Story(title="Treasure Island- Robert Louis Stevenson",
        content="Following the demise of bloodthirsty buccaneer Captain Flint, young Jim Hawkins finds himself with the key to a fortune. For he has discovered a map that will lead him to the fabled Treasure Island. But a host of villains, wild beasts and deadly savages stand between him and the stash of gold. Not to mention the most infamous pirate ever to sail the high seas . . . With a wonderfully funny introduction by award-winning author Eoin Colfer, Treasure Island is one of the twenty brilliant classic stories being reissued in Puffin Classics in March 2015.",
        rating=2)

s3 = Story(content="It's the biggest dance of the year and Nikki Maxwell is hoping her crush, Brandon, wants to be her date. But time is running out. What if he doesn't want to go with her? Or worse - what if he ends up going with Mackenzie?!! In the sixth book in the blockbuster Dork Diaries series-now with more than 13 million copies in print-join Nikki, Chloe and Zoey as they tackle the topic of love, Dork Diaries style! Rachel Ren\u00e9e Russell grew up in Saint Joseph, Michigan. She was born on December 11, 1965. She is an attorney who also writes children's books. She writes and illustrates the Dork Diaries series. Rachel wrote her first book in 6th grade as a birthday present for her younger twin brothers. Dork Diaries dramatically chronicles the daily life of the main character, Nikki Maxwell, as she struggles to fit in and survive middle school. The book series is written in a diary format and includes doodles, drawings and comic strips. According to the author's website, the Dork Diaries books are based on Rachel Renee Russell's experiences in middle school, as well as those of her two daughters, Erin and Nikki. Her older daughter, Erin, helps with writing and her younger daughter, Nikki, helps with illustrations. The main character, Nikki Maxwell, is named after her daughter. Currently, there are over 10 million copies of the Dork Diaries books in print in the United States. Publishing rights have been sold in 36 countries with translation into 32 different languages. Dork Diaries was awarded the 2010 Children's Choice Book of the Year Award for the 5th/6th grade division. She made The New York Times Best Seller List iwith her title OMG!:All about Me Diary! and her title Dork Diaries.",
            title= "DORK DIARIES: HOLIDAY HEARTBREAK #6- Rachel Renee Russell",
            rating=4)

s4 = Story(
    content = "All modern American literature comes from one book by Mark Twain called \"Huckleberry Finn.\" It's the best book we've had.\" --Ernest Hemingway Huckleberry Finn had a tough life with his drunk father until an adventure with Tom Sawyer changed everything. But when Huck's dad returns and kidnaps him, he must escpe down the Mississippi river with runaway slave, Jim. They encounter trouble at every turn, from floods and gunfights to armed bandits and the long arm of the law. Through it all the friends stick together - but can Huck and Tom free Jim from slavery once and for all? With an inspirational introduction by Darren Shan, The Adventures of Huckleberry Finn is one of the twenty wonderful classic stories being relaunched in Puffin Classics in March 2015.",
    title= "The Adventures of Huckleberry Finn - Mark Twain and Darren Shan",
    rating=5)

s5 = Story(
    content="Greg Heffley is in big trouble. School property has been damaged, and Greg is the prime suspect. But the crazy thing is, he\u2019s innocent. Or at least sort of. The authorities are closing in, but when a surprise blizzard hits, the Heffley family is trapped indoors. Greg knows that when the snow melts he\u2019s going to have to face the music, but could any punishment be worse than being stuck inside with your family for the holidays? The world has gone crazy for Jeff Kinney's Diary of a Wimpy Kid series Sun Kinney is right up there with J K Rowling as one of the bestselling children's authors on the planet Independent Hilarious! Sunday Telegraph The most hotly anticipated children's book of the year is here - Diary of a Wimpy Kid The Big Issue Jeff Kinney is a #1 New York Times bestselling author and six-time Nickelodeon Kids\u2019 Choice Award winner for Favorite Book. The 11th book in the series, Diary of a Wimpy Kid: Double Down, will release on November 1, 2016. The first-ever theatrical adaptation of Diary of a Wimpy Kid was staged by the prestigious Minneapolis Children\u2019s Theatre Company from April to June, 2016. It earned rave critical reviews and had sold out shows. Jeff has been named one of Time magazine\u2019s 100 Most Influential People in the World. He is also the creator of Poptropica, which was named one of Time magazine\u2019s 50 Best Websites. Jeff spent his childhood in the Washington, D.C., area and moved to New England in 1995. He lives with his wife and two sons in Plainville, Massachusetts, where he owns a bookstore, An Unlikely Story.", 
    title="Diary of a Wimpy Kid 6: Cabin Fever - Jeff Kinney",
    rating=4)

s6 = Story(
    content="Greg's dad, Frank, is on a mission - a mission to make this wimpy kid, well, less wimpy. All manner of 'manly' physical activities are planned, but Greg just about manages to find a way out of them. That is until military academy is is mentioned and Greg realizes that he's going to have to come up with something very special to get out of this one . . . Diary of a Wimpy Kid: The Last Straw is the third title in the bestselling Diary of a Wimpy Kid series.", 
    title="Diary of a Wimpy Kid 3 : The Last Straw- Jeff Kinney",
    rating=3)

s7 = Story(
content="Whatever you do, don't ask Greg about his summer vacation because he definitely doesn't want to talk about it... It's a brand-new year and a brand-new journal and Greg is keen to put the humiliating (and secret!) events of last summer firmly behind him. But someone knows everything - someone whose job it is to most definitely not keep anything embarrassing of Greg's private - his big brother, Rodrick. How can Greg make it through this new school year with his cool(ish) reputation intact? Diary of a Wimpy Kid: Rodrick Rules is the second title in the bestselling Diary of a Wimpy Kid series.",
 title="Diary of a Wimpy Kid 2 Rodrick Rules - Jeff Kinney",
 rating=5
)

s1.save()
Story.objects.all()