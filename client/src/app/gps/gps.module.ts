import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '@angular/material';

import { GpsComponent } from './gps.component';
import { GpsService } from './gps.service';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule
  ],
  declarations: [GpsComponent],
  providers: [
    GpsService
  ],
  exports: [GpsComponent]
})
export class GpsModule { }
