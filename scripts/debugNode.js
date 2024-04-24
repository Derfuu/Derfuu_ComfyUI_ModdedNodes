import {app} from "../../../scripts/app.js";
import {ComfyWidgets} from "../../../scripts/widgets.js";

app.registerExtension({
    name: "derfuu.Debug.ShowDataText",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "DF_To_text_(Debug)") {
            function set_text_wid(text) {
                if (this.widgets) {
                    for (let i = 0; i < this.widgets.length; i++) {
                        this.widgets[i].onRemove?.();
                    }
                    this.widgets.length = 0;
                }

                const widget = ComfyWidgets.STRING(this, "DEBUG INFO", ["STRING", {multiline: true}], app).widget;
                widget.inputEl.readOnly = true;
                widget.inputEl.style.opacity = 0.75;
                widget.value = text;
            }
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                set_text_wid.call(this, message.text);
            };
            app.graph.setDirtyCanvas(true, true);
        }
    },
});
