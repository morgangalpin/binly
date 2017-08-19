import { Formatter } from './Formatter';

export class FormatterSet {

    constructor(
        readonly formatters: Formatter[]
    ) {}

    // Return a new formatted string based on the updated values.
    public update(values : Object) : string {
        for (let formatter of this.formatters) {
            if (formatter.applies(values)) {
                return formatter.apply(values);
            }
        }
        return '';
    }

}
