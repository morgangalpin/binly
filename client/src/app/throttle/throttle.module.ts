import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';

import { ThrottleComponent } from './throttle.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [ThrottleComponent],
  exports: [ThrottleComponent],
  providers: []
})
export class ThrottleModule { }
