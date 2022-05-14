class PolygonalChain extends Figure{
    constructor(canvas, x, y, endX = [], endY = []) {
        super(canvas, x, y, false);
        this.currentX = 0;
        this.currentY = 0;

        this.endX = endX;
        this.endY = endY;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);
        for(let i = 0; i < this.endX.length; i++) {
            this.ctx.lineTo(this.endX[i], this.endY[i]);
        }
        if (this.currentX !== 0 && this.currentY !== 0)
            this.ctx.lineTo(this.currentX, this.currentY);
        this.ctx.stroke();
        this.ctx.closePath();
    }

    fix() {
        if (this.currentY === 0 && this.currentX === 0)
            return;
        this.endX.push(this.currentX);
        this.endY.push(this.currentY);
    }

    redraw(x, y) {
        this.reset();
        this.currentX = x;
        this.currentY = y;
        this.draw();
    }
}