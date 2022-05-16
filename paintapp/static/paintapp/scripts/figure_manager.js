class FigureManager {
    constructor(start_value = []) {
        this.storage = [];
        for (let i = 0; i < start_value.length; i++) {
            this.add_figure(start_value[i]);
        }
        this.id_generator = 0;
    }

    add_figure(figure_json) {
        let item = {
            'json':figure_json,
            'id': this.id_generator,
            'deleted':false
        }

        this.id_generator += 1;
        this.storage.push(item);
        console.log(this.storage);
    }

    remove_figure(id) {
        let to_remove = this.storage.find(elem => elem.id === id);
        to_remove.deleted = true;
    }

    clear() {
        this.storage = [];
    }

    clear_deleted() {
        this.storage = this.storage.filter(item => item.deleted !== true);
    }

    get_storage() {
        return this.storage;
    }
}