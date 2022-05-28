import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PpListComponent } from './pp-list.component';

describe('PpListComponent', () => {
  let component: PpListComponent;
  let fixture: ComponentFixture<PpListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PpListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PpListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
