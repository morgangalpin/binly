/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { Formatter } from './Formatter';

describe('Formatter', () => {
  it('should create an instance', () => {
    let formatter = new Formatter('template');
    expect(formatter).toBeTruthy();
  });

  it('should replace a key with a value', () => {
    let formatter = new Formatter('start {a} end');
    expect(formatter.apply({'a': 'b'})).toBe('start b end');
  });

  it('should replace all keys in a template', () => {
    let formatter = new Formatter('start {a} {a} end');
    expect(formatter.apply({'a': 'b'})).toBe('start b b end');
  });

  it('should replace multiple keys in a template', () => {
    let formatter = new Formatter('start {a} {c} end');
    expect(formatter.apply({'a': 'b', 'c': 'd'})).toBe('start b d end');
  });

  it('should only replace keys in the template', () => {
    let formatter = new Formatter('start {a} {b} end');
    expect(formatter.apply({'a': 'b'})).toBe('start b {b} end');
  });

  it('applies is true when test not supplied', () => {
    let formatter = new Formatter('start end');
    expect(formatter.applies({})).toBe(true);
  });

  it('applies is true when test returns true', () => {
    let formatter = new Formatter('start end', function (values: Object) {return true;});
    expect(formatter.applies({})).toBe(true);
  });

  it('applies is false when test returns false', () => {
    let formatter = new Formatter('start end', function (values: Object) {return false;});
    expect(formatter.applies({})).toBe(false);
  });
});
