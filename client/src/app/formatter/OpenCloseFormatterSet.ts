import { Injectable } from "@angular/core";
import { Formatter } from './Formatter';
import { FormatterSet } from './FormatterSet';

@Injectable()
export class OpenCloseFormatterSet extends FormatterSet {

    constructor(private readonly minValue: number,
                private readonly maxValue: number) {
        super([
            new Formatter('Open', function(values: Object) {
                return values['value'] !== undefined && values['value'] <= minValue;
            }),
            new Formatter('Closed by {value}', function(values: Object) {
                return values['value'] !== undefined && values['value'] > minValue && values['value'] < maxValue;
            }),
            new Formatter('Closed', function(values: Object) {
                return values['value'] !== undefined && values['value'] >= maxValue;
            }),
            new Formatter('Unknown')
        ]);
    }
}
