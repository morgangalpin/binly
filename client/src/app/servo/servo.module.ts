import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';
import { SimpleSocketService } from '../shared';

import { ServoComponent } from './servo.component';
import { ServoFormatterSet } from './ServoFormatterSet';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [ServoComponent],
  exports: [ServoComponent],
  providers: [ServoFormatterSet]
})
export class ServoModule { }
