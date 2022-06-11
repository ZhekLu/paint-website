class FigureListShower {
    constructor(div_element, item_class_type, connecting_storage, receiver) {
        this.div = div_element;
        this.item_type = item_class_type;
        this.items_list = connecting_storage;
        this.signal_receiver = receiver;
    }

    clear() {
        this.div.innerHTML = "";
    }

    update() {
        this.clear();

        for (let i = 0; i < this.items_list.length; i++) {
            let current_figure = this.items_list[i];


            let figure_label = document.createElement('label');
            figure_label.className = this.item_type;
            figure_label.textContent = current_figure.object.type;


            let item = document.createElement('button');
            item.textContent = current_figure.deleted ? 'redo' : 'undo';
            item.className = this.item_type;
            item.id = current_figure.id;
            item.onclick = function () {
                figure_state_changed(this.id);
            }
            this.div.append(figure_label, item);
        }
    }
}