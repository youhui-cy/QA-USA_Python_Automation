import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")


    def test_set_route(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Add in S8
            pass
        print("Function created for set route")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for set route")
        pass

