class Manager {
    constructor(canvas, temp_canvas, def_tool = 'line') {
        this.tool = def_tool;
        this.current_figure = null;
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
    }

    set_tool(tool) {
        this.tool = tool;
        alert('ok')
    }

    handleEvent(event) {
        // alert('ok');
        switch (event.type) {
            case 'mousedown':
                this.create(event.clientX, event.clientY);
                break;

            case 'mouseup':
                this.save();
                break;

            case 'mousemove':
                this.draw(event.clientX, event.clientY);
                break;
        }

    }

    create(mouseX, mouseY) {
        switch (this.tool) {
            case 'rectangle':
                this.current_figure = new Rectangle(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop),
                    true
                );
                break;
            case 'circle':
                this.current_figure = new Ellipse(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop),
                    true
                );
                break;
        }
    }

    save() {
        this.current_figure = null;
    }

    draw(mouseX, mouseY) {
        if (!this.current_figure)
            return;
        let x = mouseX - this.temp_canvas.offsetLeft;
        let y = mouseY - this.temp_canvas.offsetTop;
        this.current_figure.redraw(x, y);
    }
}