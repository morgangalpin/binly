import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '@angular/material';

import { GpsComponent } from './gps.component';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule
  ],
  declarations: [GpsComponent],
  exports: [GpsComponent]
})
export class GpsModule { }
