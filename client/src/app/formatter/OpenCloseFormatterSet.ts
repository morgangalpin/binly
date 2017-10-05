import { Injectable } from "@angular/core";
import { FormatterSet, Formatter } from './index';

@Injectable()
export class OpenCloseFormatterSet extends FormatterSet {

    constructor(private readonly minValue: number,
                private readonly maxValue: number) {
        super([
            new Formatter('Closed', function(values: Object) {
                return values['value'] !== undefined && values['value'] <= minValue;
            }),
            new Formatter('Open by {value}', function(values: Object) {
                return values['value'] !== undefined && values['value'] > minValue && values['value'] < maxValue;
            }),
            new Formatter('Open', function(values: Object) {
                return values['value'] !== undefined && values['value'] >= maxValue;
            }),
            new Formatter('Unknown')
        ]);
    }
}
