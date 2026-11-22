from .employee import Employee


class Driver(Employee): ...  # tutaj zaimplementuj klasę Driver


# Uruchomienie tego kodu: python -m python1course.zaj05.personnel.driver
if __name__ == "__main__":
    driver1 = Driver("Jane", "Smith", 1, 12000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
