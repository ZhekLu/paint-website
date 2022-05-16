class FigureManager {
    constructor(view_presenter = null, start_value = []) {
        this.storage = [];
        for (let i = 0; i < start_value.length; i++) {
            this.add_figure(start_value[i]);
        }
        this.id_generator = 0;

        this.view = new FigureListShower(view_presenter, 'figure_item', this.storage, this);
    }

    add_figure(figure) {
        let item = {
            'object':figure,
            'id': this.id_generator,
            'deleted':false
        }

        this.id_generator += 1;
        this.storage.push(item);
        console.log(this.storage);
        this.signal();
    }

    remove_figure(id) {
        let to_remove = this.storage.find(elem => elem.id === id);
        to_remove.deleted = true;
        this.signal();
    }

    clear() {
        this.storage.length = 0;
        this.signal();
    }

    clear_deleted() {
        this.storage = this.storage.filter(item => item.deleted !== true);
        this.signal();
    }

    get_storage() {
        return this.storage;
    }

    signal() {
        this.view.update();
    }

    figure_state_changed(id) {
        let to_change = this.storage.find(elem => elem.id == id);
        to_change.deleted = !(to_change.deleted);
        this.signal();
    }
}