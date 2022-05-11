class Manager {
    constructor(canvas, def_tool = 'line') {
        this.tool = def_tool;
        this.rect = new RectangleTool(canvas);
    }

    set_tool(tool) {
        this.tool = tool;
    }

    handleEvent(event) {
        // alert('ok');
        switch (this.tool) {
            case 'rectangle':
                this.rect.handleEvent(event);
                break;
            case 'circle':
                break;
        }

    }
}