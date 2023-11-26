import pandas as pd

def tests(test_idx):
    print(f"test{test_idx}")
    test_data = [
       [{ 
            'film': pd.DataFrame([
                (1, 'Film A'), #here
                (2, 'Film B')
            ], columns=['film_id', 'title']),

            'film_actor': pd.DataFrame([
                (1, 1, 100), #here
                (2, 2, 100)
            ], columns=['id', 'film_id', 'actor_id']),

            'actor': pd.DataFrame([
                (100, 'John', 'Doe') #here
            ], columns=['actor_id', 'first_name', 'last_name']),

            'rental': pd.DataFrame([
                 (1, 1000) #here all
                ,(2, 1000)
                ,(3, 1000)
                ,(4, 1000)

                ,(5, 1000)
                ,(6, 1000)
                ,(7, 1000)              
                ,(8, 1000)

            ], columns=['rental_id', 'inventory_id']),

            'inventory': pd.DataFrame([
                (1000, 1),  #here better same position cause if not the do it manually and time was x...
                (2000, 2)
            ], columns=['inventory_id', 'film_id']),

            'info': 4
        }]
    ]

    film = test_data[test_idx][0]['film']
    film_actor = test_data[test_idx][0]['film_actor']
    actor = test_data[test_idx][0]['actor']
    rental = test_data[test_idx][0]['rental']
    inventory = test_data[test_idx][0]['inventory']

    return film, film_actor, actor, rental, inventory

# Виклик тестових даних
#film, film_actor, actor, rental, inventory = tests(test_idx=0)


# є 7 прокатів у 1 фільма, але один фільм не був у прокаті
# є 7 прокатів у 1 фільма, але актор знявся у меншій кількості фільмів
# є 7 прокатів у 1 фільма, але є фільм з меншим прокатом

