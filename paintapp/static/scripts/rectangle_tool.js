class RectangleTool {
    constructor(canvas, temp_canvas) {
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
        this.current = null;
    }

    handleEvent(event) {
        switch (event.type) {
            case 'mousedown':
                // alert('ok');
                // this.current = new Rectangle(this.temp_canvas,
                //     (event.clientX - this.temp_canvas.offsetLeft),
                //     (event.clientY - this.temp_canvas.offsetTop),
                //     true
                // );
                this.current = new Ellipse(this.temp_canvas,
                    (event.clientX - this.temp_canvas.offsetLeft),
                    (event.clientY - this.temp_canvas.offsetTop),
                    true
                );
                break;

            case 'mouseup':
                this.current = null;
                break;

            case 'mousemove':
                if (this.current) {
                    let x = event.clientX - this.temp_canvas.offsetLeft;
                    let y = event.clientY - this.temp_canvas.offsetTop;
                    this.current.redraw(x, y);
                }
                break;
        }
    }
}

