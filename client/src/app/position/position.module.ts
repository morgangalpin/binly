import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '@angular/material';

import { PositionComponent } from './position.component';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule
  ],
  declarations: [PositionComponent],
  exports: [PositionComponent]
})
export class PositionModule { }
