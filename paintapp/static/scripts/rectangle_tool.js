class Rectangle {
    constructor(filled, x, y, height=0, width=0) {
        this.fill = filled;
        this.startX = x;
        this.startY = y;
        this.height = height;
        this.width = width;

        ctx.beginPath();
        ctx.moveTo(this.startX, this.startY);
    }

    draw() {
        ctx.beginPath();
        ctx.strokeRect(this.startX, this.startY, this.width, this.height);
        if (this.fill) {
            ctx.fillRect(this.startX, this.startY, this.width, this.height);
        }
        ctx.closePath();
    }

    redraw(width, height) {
        this.reset();
        this.height = height - this.startY;
        this.width = width - this.startX;
        this.draw();
    }

    reset() {
        ctx.clearRect(0, 0, temp_canvas.width, temp_canvas.height);
    }
}

class RectangleTool {
    constructor(canvas) {
        // this.canvas = canvas;
        this.current = null;
        this.startX = 0;
        this.startY = 0;
    }

    handleEvent(event) {
        switch (event.type) {
            case 'mousedown':
                // alert('ok');
                this.current = new Rectangle(true,
                    (event.clientX - temp_canvas.offsetLeft), (event.clientY - temp_canvas.offsetTop));
                break;

            case 'mouseup':
                this.current = null;
                break;

            case 'mousemove':
                if (this.current) {
                    let x = event.clientX - temp_canvas.offsetLeft;
                    let y = event.clientY - temp_canvas.offsetTop;
                    this.current.redraw(x, y);
                }
                break;
        }
    }
}

