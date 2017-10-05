import { Injectable } from "@angular/core";
import { FormatterSet, Formatter } from './index';

@Injectable()
export class LeftRightFormatterSet extends FormatterSet {

    constructor() {
        super([
            new Formatter('Left {value}', function(values: Object) {
                let result = values['value'] && values['value'] < 0;
                if (result) {
                    values['value'] = -values['value'];
                }
                return result;
            }),
            new Formatter('Right {value}', function(values: Object) {
                return values['value'] && values['value'] > 0;
            }),
            new Formatter('Center', function(values: Object) {
                return values['value'] !== undefined && values['value'] == 0;
            }),
            new Formatter('Unknown')
        ]);
    }
}
