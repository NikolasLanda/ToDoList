import backend


backend.add_tasks("Nakoupit mléko")
backend.add_tasks("Udělat domácí úkol")
backend.add_tasks("Vynést koš")


backend.complete_tasks(0)


backend.delete_tasks(1)


print(backend.load_tasks())