
from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)             
db = SqliteDatabase("blogs.db")
blogs = [
    {'id': 1, 'title': 'Usage of Coconut Oil to save your skin and hair', 'body': 'Coconut oil is commonly used in cosmetics and cosmeceuticals to calm itchy, dry skin and moisturize as a creamy, lotion-like oil.Benefits of coconut oil at home.How to use coconut oil for hair: Use as a pre-shampoo conditioner. Just rub a small amount of coconut oil into the dry hair and let it do its work for 20 to 30 minutes. Wash and condition hair as usual. You can also tame the frizzies. Rub ½ teaspoon coconut in your hair after styling. The oil will calm down dryness and the frizzies and give your hair a wonderful fragrance.How to use coconut oil for skin: Moisten dry lips. Rub coconut oil on your lips and then rinse it off. Coat again with the oil to keep lips moist and soft. Also, fight fungus on your feet. Did you know that coconut oil has natural anti-fungal properties? It makes a great moisturizer for your legs, feet and heels. Use it daily to keep your feet smooth and prevent foot fungus.Do you know that smoking can cause damage to your skin? Smoking causes  weakening of the skin and results to sags and bags. Women who smoke at a young age will notice sagging skin and premature wrinkles long before their nonsmoking peers.'},
    {'id': 2, 'title': 'Skin Care for Teen Skin', 'body': 'It is almost impossible to get through your teen years without a slew of complaints about your skin.Puberty in girls begins at the age of 10- 14 years.There is a fact that we all have differentskin types,this means the skin tip that works for her might not work for you. Here are the top skin tips for teen skin care: 1. Cleanse carefully. If your skin is oily, you will probably do well with a foaming or gel cleanser for daily skin care. Cleanse once a day, or twice if your skin gets very oily or dirty throughout the day e.g.If a teen girl wears makeup, it is best to remove eye makeup first, then cleanse with your fingertips and a gel or foaming cleanser.For teens who have dry rather than oily skin, try a milky cleanser and moisturizer always carry facial tissues to soak up your skin. 2. Get the right acne products. If you have breakouts wash your skin,use a toner, and then apply a medicated acne gel. 3. Don’t share makeup. Do you know it is bad to  share your friends germs? It is especially a bad idea to share eye and lip products.So, as tempting as it is to try your friends perfect new lipstick, get your own instead. 4. Keep hands clean. One way to help your skin stay healthy is to protect it from dirt and too many germs. Wash your hands before you touch your face or touch up your makeup and regularly clean other surfaces that touch your skin, such as your phone. 5.Skip the toothpaste and other old  tales. You might hear about many odd remedies to control acne, like putting toothpaste on your skin. In fact, this could just make skin worse if you are allergic to the ingredients.'}
]


class Myentry(Model):
  
    title = CharField(max_length=255, unique=True)
    body = TextField(default="Body")
   

    

    class Meta:
        database = db


def initialize():
    try:
        Myentry.create_table()
    except OperationalError:
        pass
    for blog in blogs:
        try:
            Myentry.create(
                title=blog.get('title'),
                body=blog.get('body'),
                )
        except IntegrityError:
            pass