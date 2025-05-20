import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._listCountry = self._model.getCountries()
        for n in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(n))
        self._view.update_page()
        self._listYear = self._model.getYear()
        for n in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(n))
        self._view.update_page()



    def handle_graph(self, e):
        anno = self._view.ddyear.value
        paese = self._view.ddcountry.value

        if anno is None or paese is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione! Selezionare tutti i parametri", color='red'))
            self._view.update_page()

        else:
            grafo = self._model.BuildGraph(anno, paese)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
            self._view.update_page()
            self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di archi: {self._model.getNumEdges()}"))
            self._view.update_page()



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
