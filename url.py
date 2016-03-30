# coding:utf-8


url = [(r"^/", "handlers.index.IndexHandler")]

url += [(r"^/todo/new", "handlers.new.NewHandler")]

url += [(r"^/todo/(\d+)/edit", "handlers.edit.EditHandler")]

url += [(r"^/todo/(\d+)/delete", "handlers.delete.DeleteHandler")]

url += [(r"^/todo/(\d+)/finish", "handlers.finish.FinishHandler")]
